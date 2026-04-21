class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_emails = set()
        
        for email in emails:
            # 1. Split into local and domain parts
            local, domain = email.split('@')
            
            # 2. Apply '+' rule: ignore everything after first '+'
            local = local.split('+')[0]
            
            # 3. Apply '.' rule: remove all periods
            local = local.replace('.', '')
            
            # 4. Reconstruct the "true" email and add to set
            # The set automatically ignores duplicates!
            unique_emails.add(local + '@' + domain)
            
        return len(unique_emails)